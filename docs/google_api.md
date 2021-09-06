### Service endpoint
##### https://fake.googleapis.com

### Methods
- POST /v1/documents.copy
  - request body
    ``` 
    {
        "documentId": string,
        "title": string,
        "copiedFileLocation": string
    }
    ```
  - response model
    ```
    {
        "documentId": string
    } 
    ```
    
- POST /v1/documents.text_replace
  - request body
    ``` 
    {
        "documentId": string,
        "replacements": list[Replacement]
    }
    ```
  - additional models
    - Replacement
      ```
      {
          "search": string,
          "replace": string 
      }
      ```
  - response model
    ```
    {
        "status": string ("ok"/"error")
    } 
    ```
- POST /v1/documents.download
  - request body
    ```
    {
        "documentId": string,
        "extension": string ("pdf"/"docx")
    } 
    ```
  - response model
    ```
    {
        "files": file
    } 
    ```

- POST /v1/documents.delete
  - request body
    ```
    {
        "documentId": string
    } 
    ```
  - response model
    ```
    {
        "status": string ("ok"/"error")
    } 
    ```
    