from pydantic import BaseModel,ConfigDict, ValidationError

ecommerce_schema = {
    "properties": {
        "item_title": {"type": "string"},
        "item_price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}


class SchemaNewsWebsites(BaseModel):   
    news_headline: str
    news_short_summary: str

    class Config:
        arbitrary_types_allowed = True

#class Model(BaseModel):
#    model_config = ConfigDict(arbitrary_types_allowed=True)