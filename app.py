import agenta as ag
from llama_index import Document, ServiceContext, VectorStoreIndex
from llama_index.embeddings.openai import (
    OpenAIEmbedding,
    OpenAIEmbeddingMode,
    OpenAIEmbeddingModelType,
)
from llama_index.langchain_helpers.text_splitter import (
    TokenTextSplitter,
)
from llama_index.llms import OpenAI
from llama_index.text_splitter import TokenTextSplitter

ag.init()
ag.config.register_default(
    chunk_size=ag.IntParam(1024, 256, 4096),
    chunk_overlap=ag.IntParam(20, 0, 100),
    temperature=ag.FloatParam(0.9, 0.0, 1.0),
    model=ag.MultipleChoiceParam(
        "gpt-3.5-turbo", ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]),
    response_mode=ag.MultipleChoiceParam(
        "simple_summarize", ["simple_summarize", "refine", "compact", "tree_summarize", "accumulate", "compact_accumulate"]),
)


@ag.entrypoint
def answer_qa(transcript: str, question: str):
    text_splitter = TokenTextSplitter(
        separator="\n",
        chunk_size=ag.config.chunk_size,
        chunk_overlap=ag.config.chunk_overlap,
    )
    service_context = ServiceContext.from_defaults(
        llm=OpenAI(temperature=ag.config.temperature, model=ag.config.model),
        embed_model=OpenAIEmbedding(
            mode=OpenAIEmbeddingMode.SIMILARITY_MODE,
            model=OpenAIEmbeddingModelType.ADA,
        ),
        node_parser=text_splitter,
    )
    # build a vector store index from the transcript as message documents
    index = VectorStoreIndex.from_documents(
        documents=[Document(text=transcript)], service_context=service_context
    )

    query_engine = index.as_query_engine(
        service_context=service_context, response_mode=ag.config.response_mode
    )

    response = query_engine.query(question)
    return response
