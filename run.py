from todo import app
import os
PORT = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)