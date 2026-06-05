def check_rules(user_input):

    greetings = ["hi", "hello", "hey", "hii", "hlo"]

    # Greetings
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    # Name
    elif "your name" in user_input:
        return "I am a Hybrid AI Chatbot."

    # Python
    elif "python roadmap" in user_input:
        return """
Python Roadmap:

1. Variables & Data Types
2. Operators
3. Conditional Statements
4. Loops
5. Functions
6. OOP
7. File Handling
8. Exception Handling
9. Libraries (NumPy, Pandas)
10. Projects
"""

    elif "python" in user_input:
        return """
Python is a beginner-friendly language used for:

• AI
• Data Science
• Machine Learning
• Automation
• Web Development
• Cyber Security
"""

    # Java
    elif "java roadmap" in user_input:
        return """
Java Roadmap:

1. Variables
2. Loops
3. Methods
4. Arrays
5. OOP
6. Collections
7. Exception Handling
8. JDBC
9. Spring Boot
10. Projects
"""

    elif "java" in user_input:
        return """
Java is an object-oriented programming language.

Topics:
• Variables
• Loops
• Classes
• Inheritance
• Collections
• Exception Handling
"""

    # AI
    elif "what is ai" in user_input or user_input == "ai":
        return """
AI stands for Artificial Intelligence.

It enables machines to perform tasks that normally require human intelligence.
"""

    # Machine Learning
    elif "machine learning roadmap" in user_input:
        return """
Machine Learning Roadmap:

1. Python
2. Statistics
3. NumPy
4. Pandas
5. Data Visualization
6. Machine Learning Algorithms
7. Model Evaluation
8. Projects
"""

    elif "machine learning" in user_input:
        return """
Machine Learning is a subset of AI where systems learn from data.
"""

    # Deep Learning
    elif "deep learning roadmap" in user_input:
        return """
Deep Learning Roadmap:

1. Python
2. Linear Algebra
3. Neural Networks
4. TensorFlow/PyTorch
5. CNN
6. RNN
7. Transformers
8. Projects
"""

    elif "deep learning" in user_input:
        return """
Deep Learning is a subset of Machine Learning that uses Neural Networks.
"""

    # NLP
    elif "nlp roadmap" in user_input:
        return """
NLP Roadmap:

1. Python
2. Text Processing
3. Tokenization
4. NLTK
5. SpaCy
6. Transformers
7. LLMs
"""

    elif "nlp" in user_input:
        return """
NLP stands for Natural Language Processing.

It helps computers understand human language.
"""

    # Data Science
    elif "data science roadmap" in user_input:
        return """
Data Science Roadmap:

1. Python
2. Statistics
3. SQL
4. Pandas
5. Data Visualization
6. Machine Learning
7. Projects
"""

    elif "data science" in user_input:
        return """
Data Science combines statistics, programming and business insights.
"""

    # System Design
    elif "system design roadmap" in user_input:
        return """
System Design Roadmap:

1. Computer Networks
2. Databases
3. Caching
4. Load Balancing
5. Microservices
6. Scalability
7. Design Interviews
"""

    elif "system design" in user_input:
        return """
System Design focuses on building scalable and reliable software systems.
"""

    # Web Development
    elif "web development" in user_input:
        return """
Web Development consists of:

• HTML
• CSS
• JavaScript
• React
• Node.js
• Databases
"""

    # Database
    elif "sql" in user_input or "database" in user_input:
        return """
SQL is used to manage and query relational databases such as MySQL and PostgreSQL.
"""

    # Projects
    elif "project ideas" in user_input:
        return """
Project Ideas:

1. Chatbot
2. Student Management System
3. Library Management System
4. Face Recognition System
5. Expense Tracker
"""

    # Help
    elif "help" in user_input:
        return """
You can ask me about:

• Python
• Java
• AI
• Machine Learning
• Deep Learning
• NLP
• Data Science
• System Design
• SQL
• Web Development
"""

    # Security Guardrail
    elif "password" in user_input:
        return "Sorry, I cannot provide passwords or sensitive information."

    if user_input in ["exit", "quit", "bye"]:
        return "goodbye. You can start a new conversation."

    return None