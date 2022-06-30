from __init__ import create_app, db

app_runner = create_app('config.DevConfiguration')

if __name__ == '__main__':
    ctx = app_runner.app_context()
    ctx.push()
    # Create tables
    db.create_all()
    app_runner.run(debug=True)
    ctx.pop()

