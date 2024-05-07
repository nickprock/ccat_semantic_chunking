from cat.mad_hatter.decorators import hook
from langchain_experimental.text_splitter import SemanticChunker


@hook
def rabbithole_instantiates_splitter(text_splitter, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    
    text_splitter = SemanticChunker(
        embeddings=cat.embedder,
        breakpoint_threshold_type=settings["breakpoint_threshold_type"],
        breakpoint_threshold_amount=settings["breakpoint_threshold_amount"],
    )
    return text_splitter
