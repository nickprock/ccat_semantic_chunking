# Semantic Chunking

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

Splits the text based on semantic similarity.
Check the [official LangChain documentation page](https://python.langchain.com/docs/modules/data_connection/document_transformers/semantic-chunker/)

## Settings

`breakpoint_threshold_type` must be one between:
* *"percentile"*
* *"standard_deviation"*
* *"interquartile"*
    
the recommended values by langchain for `breakpoint_threshold_amount` are:
        *"percentile"*: 95
        *"standard_deviation"*: 3
        *"interquartile"*: 1.5

![splitter](https://github.com/nickprock/ccat_semantic_chunking/blob/main/IMG_6689.png)