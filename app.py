from flask import Flask

# إنشاء تطبيق Flask
app = Flask(__name__)

# تعريف Route على الرابط الأساسي "/"
@app.route("/")
def hello():
    return {"message": "Hello from DevOps Project!"}

# تشغيل التطبيق لو الملف ده هو الملف الرئيسي
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
