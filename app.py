from flask import Flask, request, Response, redirect

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Log headers for debugging
    print(f"Request Headers: {request.headers}")

    # Get the client's IP, prioritizing X-Forwarded-For
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Handle multiple IPs in X-Forwarded-For (first is typically the client’s public IP)
    if user_ip and ',' in user_ip:
        user_ip = user_ip.split(',')[0].strip()

    # Basic validation to ensure it’s not a private IP (optional)
    if user_ip.startswith(('10.', '172.16.', '172.17.', '172.18.', '172.19.', 
                           '172.20.', '172.21.', '172.22.', '172.23.', '172.24.', 
                           '172.25.', '172.26.', '172.27.', '172.28.', '172.29.', 
                           '172.30.', '172.31.', '192.168.', '127.')):
        return Response("Could not determine public IP (private IP detected)", mimetype='text/plain')

    # Return just the plain IP as text
    return Response(user_ip, mimetype='text/plain')

# Redirect to an external favicon URL
@app.route('/favicon.ico')
def favicon():
    return redirect("https://www.google.com/s2/favicons?domain=optimumsage.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
