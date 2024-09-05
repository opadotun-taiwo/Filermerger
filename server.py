import pandas as pd
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import json

def append_files(path):
    frames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file_path)
            
            if file_extension.lower() == '.xlsx':
                df = pd.read_excel(file_path)
            elif file_extension.lower() == '.csv':
                df = pd.read_csv(file_path)
            else:
                continue  # Skip files that are neither Excel nor CSV
            
            frames.append(df)
    
    if frames:
        return pd.concat(frames, axis=0, ignore_index=True)
    else:
        return None

class FilesMergerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/merge':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            path = params['path'][0]

            try:
                merged_df = append_files(path)
                if merged_df is not None:
                    output_path = os.path.join(os.path.dirname(path), 'merged_files.xlsx')
                    merged_df.to_excel(output_path, index=False)
                    response = {'success': True, 'message': f'Files merged successfully. Output saved to {output_path}'}
                else:
                    response = {'success': False, 'message': 'No Excel or CSV files found in the specified path'}
            except Exception as e:
                response = {'success': False, 'message': f'An error occurred: {str(e)}'}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_error(404, 'Not Found')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FilesMergerHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()