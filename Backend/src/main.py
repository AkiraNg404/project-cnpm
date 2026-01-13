print(">>> MAIN.PY ĐÃ CHẠY <<<")

from flask import Flask
from src.routes.assign_routes import assign_bp

app = Flask(__name__)
app.register_blueprint(assign_bp)

if __name__ == "__main__":
    print(">>> FLASK START <<<")
    app.run(debug=True)
