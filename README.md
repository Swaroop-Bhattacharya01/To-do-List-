# 📝 To-Do List

A simple **To-Do List** web application built with **Python (Flask)**.  
Easily add, view, complete, and delete tasks. The project is configured for deployment on **Render**.

---

## 🚀 Features
- ➕ Add new tasks  
- 👀 View all tasks  
- ✅ Mark tasks as complete  
- ❌ Delete tasks  
- 🌐 Ready-to-deploy on [Render](https://render.com)  
- 🌐 Live version: [https://to-do-list-e3zi.onrender.com](https://to-do-list-e3zi.onrender.com)  
- 📄 API documentation: [https://to-do-list-e3zi.onrender.com/docs](https://to-do-list-e3zi.onrender.com/docs)  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Framework:** Flask  
- **Deployment:** Render (via `render.yaml`)  

---

## ⚙️ Running the App Locally

Follow these steps to run the site on your local machine:

### 1. Clone the Repository
```bash
**git clone [https://github.com/Swaroop-Bhattacharya01/To-do-List-.git](https://github.com/Swaroop-Bhattacharya01/To-do-List-.git)**
**cd To-do-List-**

**2. Create a Virtual Environment (Optional but Recommended)**
**python -m venv venv**
**# Activate the environment**
**# On Windows:**  
**venv\Scripts\activate**
**# On Mac/Linux:**  
**source venv/bin/activate**

**3. Install Dependencies**
**pip install -r requirements.txt**

**4. Run the Application**
**python main.py**

**5. Access the Site**

**Open your browser and go to:**

[**http://localhost:5000**](http://localhost:5000)

**You can also access the API documentation locally at:**

[**http://localhost:5000/docs**](http://localhost:5000/docs)

**🌍 Deployment (Render)**

**Push your project to GitHub**

**On Render, create a Web Service and connect the repository**

**Render will auto-detect the render.yaml file and configure the environment**

**After deployment, access the live app at: [https://to-do-list-e3zi.onrender.com](https://to-do-list-e3zi.onrender.com)**

**🛠️ How to Use the Live API**

**You can interact with the live API at [https://to-do-list-e3zi.onrender.com/docs](https://to-do-list-e3zi.onrender.com/docs)
using the Swagger UI. Follow these steps:**

**1. Open the API UI**

**Visit:**
**[https://to-do-list-e3zi.onrender.com/docs](https://to-do-list-e3zi.onrender.com/docs)**

**2. Create a User**

**Endpoint: POST /users/**

**Example request body:**

{
"username": "alice",
"password": "StrongPass123"
}


**3. Get an Access Token**

**Endpoint: POST /token**

**Fill in the Try it out form with your username and password:**

**username: alice**
**password: StrongPass123**

**Copy the access_token from the response.**

**4. Authorize in Swagger**

**Click Authorize in the Swagger UI.**

**Enter your token as:**

**Bearer YOUR_ACCESS_TOKEN**

**Click Authorize and then Close.**

**5. Use the Todos Endpoints**

**Get all tasks: GET /todos/**

**Add a task: POST /todos/**
**Example body:**

{
"title": "My first task",
"description": "optional",
"completed": false
}


**Update a task: PUT /todos/{todo_id}**

**Delete a task: DELETE /todos/{todo_id}**

**✅ Tips:**

**Always authorize before using protected endpoints.**

**You can manage multiple users and tasks independently.**

**🤝 Contributing**

**Contributions are welcome!**

**Fork the project**

**Create a feature branch (git checkout -b feature/new-feature)**

**Commit your changes (git commit -m "Add new feature")**

**Push to your fork (git push origin feature/new-feature)**

**Open a Pull Request**
