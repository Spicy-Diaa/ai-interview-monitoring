# question_bank.py
# بنك الأسئلة التقنية لنظام Hire Path
# الهيكل: QUESTION_BANK[التخصص][المستوى] = قايمة أسئلة

QUESTION_BANK = {
    "Front-End Developer": {
        "Beginner": [
            {
                "question": "What is the difference between HTML, CSS, and JavaScript?",
                "model_answer": "HTML defines the structure and content of a web page. CSS controls the style and layout, such as colors and spacing. JavaScript adds interactivity and behavior, like responding to clicks.",
                "keywords": ["structure", "content", "style", "layout", "interactivity", "behavior"],
            },
            {
                "question": "What is the CSS box model?",
                "model_answer": "Every HTML element is a box made of content, padding, border, and margin. Padding is the space inside the border, and margin is the space outside it.",
                "keywords": ["content", "padding", "border", "margin", "box"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is the difference between let, const, and var in JavaScript?",
                "model_answer": "var is function scoped and can be redeclared. let is block scoped and can be reassigned. const is block scoped and cannot be reassigned. let and const are preferred in modern code.",
                "keywords": ["scope", "block", "function", "reassign", "redeclare", "hoisting"],
            },
            {
                "question": "What is the Virtual DOM in React and why is it useful?",
                "model_answer": "The Virtual DOM is a lightweight copy of the real DOM kept in memory. React compares the new version with the old one (diffing) and updates only the parts that changed, which improves performance.",
                "keywords": ["virtual dom", "diffing", "update", "performance", "real dom", "render"],
            },
        ],
        "Advanced": [
            {
                "question": "How would you improve the performance of a slow web page?",
                "model_answer": "Minimize and compress files, use lazy loading for images, use caching and a CDN, split code into smaller bundles, reduce unnecessary re-renders, and measure with tools like Lighthouse.",
                "keywords": ["lazy loading", "caching", "cdn", "minify", "code splitting", "lighthouse", "bundle"],
            },
            {
                "question": "Explain closures and the event loop in JavaScript.",
                "model_answer": "A closure is a function that remembers variables from its outer scope even after the outer function finished. The event loop lets JavaScript handle async tasks: it runs the call stack first, then picks callbacks from the queue when the stack is empty.",
                "keywords": ["closure", "scope", "event loop", "call stack", "callback", "queue", "async"],
            },
        ],
    },    "Python Back-End Developer": {
        "Beginner": [
            {
                "question": "What is the difference between a list and a tuple in Python?",
                "model_answer": "A list is mutable, so you can change its items after creation. A tuple is immutable, so it cannot be changed. Tuples are slightly faster and can be used as dictionary keys.",
                "keywords": ["mutable", "immutable", "list", "tuple", "change", "faster"],
            },
            {
                "question": "What is an API and what is REST?",
                "model_answer": "An API lets two programs communicate with each other. REST is a style of building APIs that uses HTTP methods like GET, POST, PUT, and DELETE to work with resources identified by URLs.",
                "keywords": ["api", "rest", "http", "get", "post", "put", "delete", "resource", "url"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is the difference between Django and Flask?",
                "model_answer": "Django is a full-featured framework that includes an ORM, authentication, and an admin panel out of the box. Flask is a lightweight micro-framework that gives more flexibility, and you add the extensions you need.",
                "keywords": ["django", "flask", "orm", "admin", "lightweight", "framework", "flexibility"],
            },
            {
                "question": "What is an ORM and why do we use it?",
                "model_answer": "An ORM maps database tables to Python classes, so you can work with the database using Python objects instead of raw SQL. It improves productivity, reduces SQL mistakes, and helps prevent SQL injection.",
                "keywords": ["orm", "database", "table", "class", "object", "sql", "injection", "model"],
            },
        ],
        "Advanced": [
            {
                "question": "How do you secure a REST API?",
                "model_answer": "Use HTTPS, authenticate users with tokens such as JWT or OAuth, authorize access by role, validate all inputs, apply rate limiting, and protect against SQL injection and CORS misconfiguration.",
                "keywords": ["https", "jwt", "oauth", "authentication", "authorization", "rate limiting", "validation", "cors"],
            },
            {
                "question": "How can you improve the performance of a backend application?",
                "model_answer": "Add caching with Redis, optimize database queries and add indexes, use pagination, run slow tasks in the background with a queue like Celery, use async code, and apply load balancing.",
                "keywords": ["caching", "redis", "index", "query", "pagination", "celery", "async", "load balancing"],
            },
        ],
    },    "Data Analyst": {
        "Beginner": [
            {
                "question": "What is the difference between a primary key and a foreign key in SQL?",
                "model_answer": "A primary key uniquely identifies each row in a table and cannot be null. A foreign key is a column that refers to the primary key of another table and is used to link tables together.",
                "keywords": ["primary key", "foreign key", "unique", "table", "link", "relationship", "null"],
            },
            {
                "question": "What is data cleaning and why is it important?",
                "model_answer": "Data cleaning means fixing or removing incorrect, duplicate, missing, or inconsistent data. It is important because analysis on dirty data gives wrong and misleading results.",
                "keywords": ["missing", "duplicate", "inconsistent", "errors", "accuracy", "quality", "outliers"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is the difference between INNER JOIN and LEFT JOIN?",
                "model_answer": "INNER JOIN returns only the rows that match in both tables. LEFT JOIN returns all rows from the left table and the matching rows from the right table, with NULL where there is no match.",
                "keywords": ["inner join", "left join", "match", "null", "rows", "left table", "right table"],
            },
            {
                "question": "How do you handle missing values in a dataset using Pandas?",
                "model_answer": "First detect them with isnull() and sum(). Then either remove them with dropna() or fill them with fillna() using the mean, median, or a fixed value, depending on the data and how much is missing.",
                "keywords": ["isnull", "dropna", "fillna", "mean", "median", "missing", "pandas"],
            },
        ],
        "Advanced": [
            {
                "question": "What is the difference between WHERE and HAVING in SQL, and what are window functions?",
                "model_answer": "WHERE filters rows before grouping, and HAVING filters groups after GROUP BY. Window functions such as ROW_NUMBER, RANK, and SUM OVER perform calculations across related rows without collapsing them into one row.",
                "keywords": ["where", "having", "group by", "window function", "row_number", "rank", "over", "partition"],
            },
            {
                "question": "How would you design a dashboard to present insights to business stakeholders?",
                "model_answer": "Start by understanding the business goal and the key KPIs. Choose suitable charts for each metric, keep the design simple and clear, add filters for interactivity, and focus on telling a story with the data using tools like Power BI or Tableau.",
                "keywords": ["kpi", "business goal", "visualization", "chart", "filter", "storytelling", "power bi", "tableau"],
            },
        ],
    },    "Mobile App Developer": {
        "Beginner": [
            {
                "question": "What is the difference between native apps and cross-platform apps?",
                "model_answer": "Native apps are built for one platform using its own language, such as Swift for iOS and Kotlin for Android, and give the best performance. Cross-platform apps use one codebase for both platforms with tools like Flutter or React Native, which saves time and cost.",
                "keywords": ["native", "cross-platform", "swift", "kotlin", "flutter", "react native", "codebase", "performance"],
            },
            {
                "question": "What is an Activity in Android or a ViewController in iOS?",
                "model_answer": "It is a single screen of the app that the user interacts with. It handles the user interface and the user actions for that screen, and it has a lifecycle that the system manages.",
                "keywords": ["screen", "activity", "viewcontroller", "interface", "lifecycle", "user"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is the difference between StatelessWidget and StatefulWidget in Flutter?",
                "model_answer": "A StatelessWidget does not change after it is built. A StatefulWidget has a State object that can change over time, and calling setState rebuilds the widget with the new data.",
                "keywords": ["stateless", "stateful", "state", "setstate", "rebuild", "widget", "change"],
            },
            {
                "question": "How does a mobile app communicate with a backend server?",
                "model_answer": "The app sends HTTP requests to a REST API and receives data in JSON format. The requests are asynchronous so the interface does not freeze, and authentication is done with tokens.",
                "keywords": ["http", "rest", "api", "json", "asynchronous", "token", "request", "response"],
            },
        ],
        "Advanced": [
            {
                "question": "How do you manage state in a large mobile application?",
                "model_answer": "Use a state management solution such as Provider, Bloc, or Riverpod in Flutter, or Redux in React Native. Separate the business logic from the user interface using an architecture like MVVM or Clean Architecture, which makes the app easier to test and maintain.",
                "keywords": ["state management", "provider", "bloc", "riverpod", "redux", "mvvm", "architecture", "testing"],
            },
            {
                "question": "How do you improve the performance and offline support of a mobile app?",
                "model_answer": "Cache data locally using SQLite or Hive, load images lazily, avoid unnecessary rebuilds, use pagination for long lists, and sync data with the server when the connection returns.",
                "keywords": ["cache", "sqlite", "hive", "lazy loading", "pagination", "offline", "sync", "performance"],
            },
        ],
    },
    "DevOps Engineer": {
        "Beginner": [
            {
                "question": "What is DevOps?",
                "model_answer": "DevOps is a culture and set of practices that bring development and operations teams together. It aims to deliver software faster and more reliably through automation, collaboration, and continuous feedback.",
                "keywords": ["development", "operations", "automation", "collaboration", "faster", "continuous", "delivery"],
            },
            {
                "question": "What is Docker and why do we use it?",
                "model_answer": "Docker packages an application with all its dependencies into a container, so it runs the same way on any machine. Containers are lightweight and fast compared to virtual machines.",
                "keywords": ["container", "image", "dependencies", "lightweight", "virtual machine", "portable", "docker"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is a CI/CD pipeline?",
                "model_answer": "Continuous Integration automatically builds and tests code every time a developer pushes changes. Continuous Delivery or Deployment automatically releases the tested code to staging or production. Tools include GitHub Actions and Jenkins.",
                "keywords": ["continuous integration", "continuous delivery", "build", "test", "deploy", "pipeline", "jenkins", "github actions"],
            },
            {
                "question": "What is the difference between a Docker image and a container?",
                "model_answer": "An image is a read-only template that contains the application and its dependencies. A container is a running instance of an image. You can create many containers from one image.",
                "keywords": ["image", "container", "template", "instance", "read-only", "running", "dockerfile"],
            },
        ],
        "Advanced": [
            {
                "question": "What is Kubernetes and what problems does it solve?",
                "model_answer": "Kubernetes is a platform that orchestrates containers. It handles deployment, scaling, load balancing, and self-healing. Main concepts include pods, deployments, services, and nodes.",
                "keywords": ["orchestration", "pod", "deployment", "service", "scaling", "self-healing", "load balancing", "node"],
            },
            {
                "question": "What is Infrastructure as Code and how do you monitor a production system?",
                "model_answer": "Infrastructure as Code manages servers and cloud resources using code files with tools like Terraform or Ansible, which makes setups repeatable and version controlled. For monitoring, use tools like Prometheus and Grafana to track metrics, logs, and alerts.",
                "keywords": ["infrastructure as code", "terraform", "ansible", "version control", "prometheus", "grafana", "metrics", "logs", "alerts"],
            },
        ],
    },
    "Machine Learning Engineer": {
        "Beginner": [
            {
                "question": "What is the difference between supervised and unsupervised learning?",
                "model_answer": "Supervised learning trains a model on labeled data to predict known outputs, such as classification and regression. Unsupervised learning finds patterns in unlabeled data, such as clustering.",
                "keywords": ["supervised", "unsupervised", "labeled", "unlabeled", "classification", "regression", "clustering"],
            },
            {
                "question": "What is overfitting and how can you avoid it?",
                "model_answer": "Overfitting happens when a model learns the training data too well, including the noise, and performs badly on new data. You can avoid it with more data, regularization, cross-validation, and simpler models.",
                "keywords": ["overfitting", "training data", "noise", "new data", "regularization", "cross-validation", "generalization"],
            },
        ],
        "Intermediate": [
            {
                "question": "How do you evaluate a classification model?",
                "model_answer": "Split the data into training and test sets. Use metrics such as accuracy, precision, recall, F1-score, and the confusion matrix. For imbalanced data, accuracy alone is misleading, so precision and recall are more important.",
                "keywords": ["accuracy", "precision", "recall", "f1", "confusion matrix", "test set", "imbalanced"],
            },
            {
                "question": "What is the difference between bias and variance?",
                "model_answer": "High bias means the model is too simple and underfits the data. High variance means the model is too complex and overfits the data. The goal is to find a balance between them, known as the bias-variance tradeoff.",
                "keywords": ["bias", "variance", "underfitting", "overfitting", "tradeoff", "complexity", "balance"],
            },
        ],
        "Advanced": [
            {
                "question": "Explain how a neural network learns.",
                "model_answer": "Data passes forward through layers of neurons with weights and activation functions to produce a prediction. A loss function measures the error. Backpropagation computes the gradients, and an optimizer such as gradient descent updates the weights to reduce the loss.",
                "keywords": ["layers", "weights", "activation", "loss function", "backpropagation", "gradient descent", "optimizer", "forward"],
            },
            {
                "question": "How do you deploy a machine learning model to production and monitor it?",
                "model_answer": "Save the trained model, then serve it through an API using tools like FastAPI or Flask, packaged in Docker. Monitor its performance over time and watch for data drift and concept drift, then retrain the model when needed. This process is part of MLOps.",
                "keywords": ["api", "fastapi", "docker", "monitoring", "data drift", "retrain", "mlops", "deployment"],
            },
        ],
    },
}
