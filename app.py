from app import createApp
app = createApp()

if __name__ == "__main__":
    app.run(port=5001, debug=True)