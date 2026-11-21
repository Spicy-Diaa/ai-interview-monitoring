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
    },
}
