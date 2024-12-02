from app import create_app
from app.routes import create_routes

app = create_app()
create_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
