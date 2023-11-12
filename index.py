from langchain.llms import OpenAI
from langchain.vectorstores.cassandra import Cassandra
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes.vectorstore import VectorStoreIndexWrapper

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from datasets import load_dataset


OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

ASTRA_DB_SECURE_BUNDLE_PATH = "YOUR_ASTRA_DB_SECURE_BUNDLE_PATH"
ASTRA_DB_APPLICATION_TOKEN = "YOUR_ASTRA_DB_APPLICATION_TOKEN"
ASTRA_DB_CLIENT_ID = "YOUR_ASTRA_DB_CLIENT_ID"
ASTRA_DB_CLIENT_SECRET = "YOUR_ASTRA_DB_CLIENT_SECRET"

cloud_config= {
        'secure_connect_bundle': ASTRA_DB_SECURE_BUNDLE_PATH
}

auth_provider = PlainTextAuthProvider(ASTRA_DB_CLIENT_ID, ASTRA_DB_CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

#configure openAI
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

#configure cassandra
myCassandraVStore = Cassandra(
    embedding=myEmbedding,
    session=session,
    #keyspace= "search",
    table="qa_mini_demo"
)


#load dataset
print("Loading dataset...")
myDataset = load_dataset("Biddls/Onion_News", split="train")
data = myDataset["text"][:50]

print("Generating embeddings and storing in AstraDB...")
myCassandraVStore.add_texts(data)

vectorIndex = VectorStoreIndexWrapper(vectorstore=myCassandraVStore)

#question loop
first_question = True

while True:
    if first_question:
        query_text = input("Hello there! Ask me a question (or type 'quit' to exit): ")
        first_question = False
    else:
        query_text = input("Ask me another question (or type 'quit' to exit): ")
    if query_text.lower() == 'quit':
        break

    print("QUESTION: \"%s\"" % query_text)
    answer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)

    print("DOCUMENTS BY RELEVANCE:")
    for doc, score in myCassandraVStore.similarity_search_with_score(query_text, llm=llm, k=4):
        print("  %0.4f \"%s ...\"" % (score, doc.page_content[:60]))

