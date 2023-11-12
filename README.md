# LangChain Demo

This Python script demonstrates the integration of various language models, vector stores, and embeddings using LangChain. The script interacts with a Cassandra database to store and retrieve text data, generates embeddings using OpenAI, and performs similarity searches using a vector store.


# Dependencies
1. Make sure to install the required Python packages using:

    ```bash 
    from langchain.llms import OpenAI
    from langchain.vectorstores.cassandra import Cassandra
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.indexes.vectorstore import VectorStoreIndexWrapper

    from cassandra.cluster import Cluster
    from cassandra.auth import PlainTextAuthProvider

    from datasets import load_dataset
    ```
2. Clone or download this repository:
    ```bash
    git clone https://github.com/TheFourthKaramazov/AI_Assistant
    ```

3. Replace the placeholders in the script with your actual API keys and configurations.
Before running the script, ensure you have the required API keys and configurations for OpenAI and AstraDB. Replace the placeholders in the script with your actual API keys and configuration details.

    ```python
    OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

    ASTRA_DB_SECURE_BUNDLE_PATH = "YOUR_ASTRA_DB_SECURE_BUNDLE_PATH"
    ASTRA_DB_APPLICATION_TOKEN = "YOUR_ASTRA_DB_APPLICATION_TOKEN"
    ASTRA_DB_CLIENT_ID = "YOUR_ASTRA_DB_CLIENT_ID"
    ASTRA_DB_CLIENT_SECRET = "YOUR_ASTRA_DB_CLIENT_SECRET"
    ```
## Run the script:

    ```bash
    python index.py
    ```
The script will prompt you to ask questions, and it will provide answers based on the stored text data in the AstraDB database. You can type 'quit' to exit the script.

Note: Ensure that your AstraDB database is properly configured and accessible. Make sure to replace the placeholders with your actual AstraDB details in the script.
