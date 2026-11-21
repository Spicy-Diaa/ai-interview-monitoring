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
    },    "UI/UX Designer": {
        "Beginner": [
            {
                "question": "What is the difference between UI and UX design?",
                "model_answer": "UI design focuses on how the product looks, such as colors, typography, buttons, and layout. UX design focuses on how the product works and feels for the user, including ease of use, user flow, and solving the user's problems.",
                "keywords": ["ui", "ux", "visual", "look", "usability", "user experience", "interface", "flow"],
            },
            {
                "question": "What is a wireframe and why do we use it?",
                "model_answer": "A wireframe is a simple low-fidelity sketch of a screen that shows the layout and structure without colors or final design. It helps teams agree on the structure early and saves time before the detailed design.",
                "keywords": ["wireframe", "layout", "structure", "low-fidelity", "sketch", "early", "prototype"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is user research and which methods can you use?",
                "model_answer": "User research is understanding the needs, behavior, and problems of users. Common methods include interviews, surveys, usability testing, and observation. It helps make design decisions based on real data instead of assumptions.",
                "keywords": ["user research", "interviews", "surveys", "usability testing", "needs", "behavior", "personas", "data"],
            },
            {
                "question": "What is the difference between a low-fidelity and a high-fidelity prototype?",
                "model_answer": "A low-fidelity prototype is a simple and quick version used to test ideas and structure. A high-fidelity prototype looks and behaves very close to the final product, with real colors, content, and interactions, and is used for detailed testing. Tools like Figma are commonly used.",
                "keywords": ["low-fidelity", "high-fidelity", "prototype", "interaction", "testing", "figma", "final product"],
            },
        ],
        "Advanced": [
            {
                "question": "How do you design an accessible interface?",
                "model_answer": "Use enough color contrast, do not rely on color alone to give information, support keyboard navigation and screen readers, use readable font sizes, and add text alternatives for images. Follow standards such as WCAG.",
                "keywords": ["accessibility", "contrast", "wcag", "screen reader", "keyboard", "alt text", "font size", "inclusive"],
            },
            {
                "question": "What is a design system and how do you measure the success of a design?",
                "model_answer": "A design system is a collection of reusable components, styles, and guidelines that keeps the product consistent and speeds up work. Success is measured with usability testing, A/B testing, and metrics such as task completion rate, time on task, and user satisfaction.",
                "keywords": ["design system", "components", "consistency", "reusable", "a/b testing", "usability", "metrics", "task completion"],
            },
        ],
    },
    "Cybersecurity Analyst": {
        "Beginner": [
            {
                "question": "What is the CIA triad in cybersecurity?",
                "model_answer": "The CIA triad stands for Confidentiality, Integrity, and Availability. Confidentiality means only authorized people can access data. Integrity means data is not changed without permission. Availability means systems and data are accessible when needed.",
                "keywords": ["confidentiality", "integrity", "availability", "authorized", "data", "access"],
            },
            {
                "question": "What is the difference between a virus, a worm, and a trojan?",
                "model_answer": "A virus attaches itself to a file and spreads when the file is run. A worm spreads by itself across networks without user action. A trojan pretends to be a useful program but contains malicious code.",
                "keywords": ["virus", "worm", "trojan", "malware", "spread", "malicious", "network"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is SQL injection and how can you prevent it?",
                "model_answer": "SQL injection is an attack where the attacker inserts malicious SQL code into an input field to access or change the database. It is prevented by using parameterized queries or prepared statements, validating inputs, and using least privilege for database accounts.",
                "keywords": ["sql injection", "input", "parameterized", "prepared statements", "validation", "database", "least privilege"],
            },
            {
                "question": "What is the difference between symmetric and asymmetric encryption?",
                "model_answer": "Symmetric encryption uses one shared key for both encryption and decryption and is fast, like AES. Asymmetric encryption uses a public key and a private key, like RSA, and is used for secure key exchange and digital signatures.",
                "keywords": ["symmetric", "asymmetric", "public key", "private key", "aes", "rsa", "encryption", "decryption"],
            },
        ],
        "Advanced": [
            {
                "question": "Explain the main steps of a penetration test.",
                "model_answer": "The main steps are planning and scoping, reconnaissance, scanning and vulnerability discovery, exploitation, post-exploitation, and reporting. The final report explains the findings and recommends fixes. The test must be done with written permission.",
                "keywords": ["reconnaissance", "scanning", "exploitation", "reporting", "scope", "permission", "vulnerability", "post-exploitation"],
            },
            {
                "question": "How do you respond to a security incident?",
                "model_answer": "Follow an incident response process: preparation, detection and analysis, containment, eradication, recovery, and lessons learned. Isolate affected systems, preserve logs and evidence, remove the threat, restore systems safely, and document everything. Tools such as a SIEM help with detection.",
                "keywords": ["incident response", "detection", "containment", "eradication", "recovery", "lessons learned", "siem", "logs"],
            },
        ],
    },
    "QA Engineer": {
        "Beginner": [
            {
                "question": "What is the difference between manual testing and automated testing?",
                "model_answer": "Manual testing is done by a person who runs the test steps by hand and is good for exploratory and usability testing. Automated testing uses scripts and tools such as Selenium to run tests automatically, which is faster and better for repetitive tests.",
                "keywords": ["manual", "automated", "scripts", "selenium", "repetitive", "exploratory", "faster"],
            },
            {
                "question": "What is a test case and what does it contain?",
                "model_answer": "A test case is a set of steps used to check that a feature works correctly. It contains an ID, description, preconditions, test steps, test data, expected result, and actual result.",
                "keywords": ["test case", "steps", "expected result", "actual result", "preconditions", "test data", "id"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is the difference between smoke testing and regression testing?",
                "model_answer": "Smoke testing is a quick check of the main functions to see if a build is stable enough for further testing. Regression testing checks that new changes did not break existing features.",
                "keywords": ["smoke", "regression", "build", "stable", "existing features", "new changes", "main functions"],
            },
            {
                "question": "What information should a good bug report include?",
                "model_answer": "A good bug report includes a clear title, steps to reproduce, expected result, actual result, severity and priority, environment details, and screenshots or logs.",
                "keywords": ["title", "steps to reproduce", "expected", "actual", "severity", "priority", "environment", "screenshot"],
            },
        ],
        "Advanced": [
            {
                "question": "How do you design an automation testing strategy for a project?",
                "model_answer": "Decide what to automate: stable, repetitive, and high-risk tests. Follow the test pyramid with many unit tests, fewer API tests, and few UI tests. Use a framework like Selenium with a Page Object Model, and integrate the tests into a CI/CD pipeline.",
                "keywords": ["test pyramid", "selenium", "page object model", "ci/cd", "framework", "repetitive", "high-risk", "api tests"],
            },
            {
                "question": "What is the difference between severity and priority, and how do you do performance testing?",
                "model_answer": "Severity is how serious the impact of the bug is on the system. Priority is how urgently it should be fixed. Performance testing checks speed and stability under load using tools such as JMeter, including load testing and stress testing.",
                "keywords": ["severity", "priority", "impact", "urgency", "performance", "load testing", "stress testing", "jmeter"],
            },
        ],
    },    "Database Administrator": {
        "Beginner": [
            {
                "question": "What is a database and what is the difference between SQL and NoSQL databases?",
                "model_answer": "A database is an organized collection of data. SQL databases such as MySQL and PostgreSQL store data in tables with a fixed schema and use SQL. NoSQL databases such as MongoDB store data in flexible formats like documents and are good for unstructured data and easy scaling.",
                "keywords": ["database", "sql", "nosql", "tables", "schema", "mysql", "postgresql", "mongodb", "flexible"],
            },
            {
                "question": "What is a primary key and why is it important?",
                "model_answer": "A primary key is a column or a set of columns that uniquely identifies each row in a table. It cannot be null or duplicated, and it is used to link tables and find rows quickly.",
                "keywords": ["primary key", "unique", "row", "null", "duplicate", "identify", "table"],
            },
        ],
        "Intermediate": [
            {
                "question": "What is an index and when should you use it?",
                "model_answer": "An index is a data structure that makes searching in a table faster, like the index of a book. It is useful for columns used in WHERE and JOIN conditions. However, too many indexes slow down insert and update operations and use more storage.",
                "keywords": ["index", "faster", "search", "where", "join", "slow", "insert", "update", "storage"],
            },
            {
                "question": "What is database normalization?",
                "model_answer": "Normalization is organizing data into separate related tables to reduce duplication and avoid inconsistency. It follows rules called normal forms such as 1NF, 2NF, and 3NF. Too much normalization can make queries slower because they need more joins.",
                "keywords": ["normalization", "duplication", "redundancy", "normal forms", "1nf", "2nf", "3nf", "consistency", "joins"],
            },
        ],
        "Advanced": [
            {
                "question": "What are ACID properties and what is a transaction?",
                "model_answer": "A transaction is a group of operations that run as one unit. ACID stands for Atomicity, Consistency, Isolation, and Durability. Atomicity means all or nothing, consistency keeps data valid, isolation keeps transactions from affecting each other, and durability means committed data is not lost.",
                "keywords": ["transaction", "acid", "atomicity", "consistency", "isolation", "durability", "commit", "rollback"],
            },
            {
                "question": "How do you plan backup, recovery, and performance tuning for a production database?",
                "model_answer": "Take regular full and incremental backups, store copies in a different location, and test the restore process. Use replication for high availability. For performance, analyze slow queries with EXPLAIN, add suitable indexes, and monitor resources like CPU, memory, and disk.",
                "keywords": ["backup", "recovery", "restore", "replication", "high availability", "explain", "slow queries", "index", "monitoring"],
            },
        ],
    },
    "Full-Stack Developer": {
        "Beginner": [
            {
                "question": "What is the difference between front-end and back-end development?",
                "model_answer": "Front-end is the part the user sees and interacts with in the browser, built with HTML, CSS, and JavaScript. Back-end runs on the server and handles business logic, databases, and authentication. A full-stack developer works on both.",
                "keywords": ["front-end", "back-end", "browser", "server", "database", "logic", "html", "css", "javascript"],
            },
            {
                "question": "What is the difference between GET and POST HTTP methods?",
                "model_answer": "GET is used to request and read data and does not change anything on the server. POST is used to send data to the server to create something new, and the data is sent in the request body.",
                "keywords": ["get", "post", "http", "request", "read", "create", "body", "server"],
            },
        ],
        "Intermediate": [
            {
                "question": "How does a React front-end communicate with a Node.js back-end?",
                "model_answer": "React sends HTTP requests using fetch or axios to REST API endpoints built with Node.js and Express. The server processes the request, talks to the database such as MongoDB, and returns JSON data that React displays in the interface.",
                "keywords": ["react", "node", "express", "api", "fetch", "axios", "json", "mongodb", "endpoint"],
            },
            {
                "question": "What is the difference between authentication and authorization?",
                "model_answer": "Authentication verifies who the user is, for example with a login using a password or token. Authorization decides what that user is allowed to do or access, for example admin versus normal user permissions.",
                "keywords": ["authentication", "authorization", "login", "token", "jwt", "permissions", "role", "identity"],
            },
        ],
        "Advanced": [
            {
                "question": "How would you design and deploy a scalable full-stack application?",
                "model_answer": "Separate the front-end, back-end API, and database. Use caching and a load balancer, add database indexes, and containerize the app with Docker. Set up a CI/CD pipeline for automatic testing and deployment, and add monitoring and logging.",
                "keywords": ["scalable", "load balancer", "caching", "docker", "ci/cd", "database", "monitoring", "logging", "api"],
            },
            {
                "question": "How do you secure a full-stack web application?",
                "model_answer": "Use HTTPS, hash passwords, and protect APIs with JWT or session authentication and role-based authorization. Validate and sanitize all inputs to prevent SQL injection and XSS, use CSRF protection, configure CORS correctly, and never store secrets in the front-end code.",
                "keywords": ["https", "hash", "jwt", "authorization", "sql injection", "xss", "csrf", "cors", "validation"],
            },
        ],
    },
}
