from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os

endpoint=os.environ["ENDPOINT_URL"]
key=os.environ["ENDPOINT_KEY"]


url = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-receipt", url)
receipts = poller.result()

## Retrieve items

for idx, receipt in enumerate(receipts.documents):
    merchant_name = receipt.fields.get("MerchantName")
    date_of_buy = receipt.fields.get("TransactionDate")
    print(merchant_name.value)
    print(date_of_buy.value)
