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
    },
}
