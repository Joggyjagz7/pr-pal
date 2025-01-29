# Proactive Repair Pal 🛠️👷‍♀️  

## Overview  
**Proactive Repair Pal** is a Streamlit-based chatbot designed to track user tasks and complaints using reference IDs. It provides real-time updates to enhance user experience and efficiency. The chatbot leverages **LlamaIndex**, **OpenAI's GPT-3.5-turbo**, and **LangChain** to process and respond to user queries.  

---

## Features  
- **Task Tracking**: Monitors user complaints/tasks with reference IDs.  
- **Real-time Updates**: Provides instant responses based on indexed data.  
- **Chat History**: Maintains a session-based chat log for continuity.  
- **Efficient Query Handling**: Uses **LlamaIndex** for vector-based search and retrieval.  

---

## Installation  

### Prerequisites  
Ensure you have Python **3.8+** installed on your system.  

### Clone the Repository  
```bash
git clone https://github.com/your-repo/proactive-repair-pal.git
cd proactive-repair-pal
```

### Install Dependencies  
```bash
pip install -r requirements.txt
```

### Set Up OpenAI API Key  
Replace `your_openai_api_key` with your actual OpenAI API key.  
```bash
export OPENAI_API_KEY="your_openai_api_key"
```
Or, modify the script directly:  
```python
os.environ['OPENAI_API_KEY'] = "your_openai_api_key"
```

---

## Running the Application  
```bash
streamlit run app.py
```

This will launch the chatbot interface in your default web browser.  

---

## Project Structure  
```
/proactive-repair-pal
│── /data              # Directory containing documents for indexing
│── app.py             # Main Streamlit application
│── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## How It Works  
1. **Loads Data**: The chatbot reads documents from the `/data` directory using `SimpleDirectoryReader`.  
2. **Indexes Data**: Uses **LlamaIndex** to create a searchable vector index.  
3. **Chat Engine**: Processes user queries and retrieves relevant responses.  
4. **Chat Session**: Maintains a chat history for contextual conversation.  

---

## Customization  
- Modify the **system prompt** in `ServiceContext.from_defaults()` to change the chatbot’s behavior.  
- Adjust **temperature** in the `OpenAI` model to control response randomness.  

---

## Known Issues  
- Initial data loading may take time depending on the number of documents.  
- Requires a valid OpenAI API key for functionality.  

---

## Future Enhancements  
- Integration with external **task management systems** for seamless tracking.  
- **Multilingual support** for broader accessibility.  
- Improved **UI/UX enhancements** with Streamlit components.  

