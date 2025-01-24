
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cr-arunkumar/langchain-examples.git
   ```

2. Navigate to the project directory:
   ```bash
   cd langchain-examples
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. Install the required packages:
   ```bash
   pip install langchain_groq
   //or 
   pip3 install langchain
   ```

## Usage

To use the ChatGroq model, you can create an instance as follows:
```python
from langchain_groq import ChatGroq

# Create an instance of ChatGroq
llm = ChatGroq(model="llama-3.3-70b-versatile")
```

## .gitignore

Make sure to include the following in your `.gitignore` file to avoid committing unnecessary files:

```
.venv
```