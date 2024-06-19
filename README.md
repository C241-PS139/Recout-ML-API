# Recout-ML-API

Description....

**Method:**
>POST

- **Recommendation Model**
```bash
POST {{Host}}/recommend
```

## Step
1. Clone the git repository.
```bash
git clone https://github.com/C23-PS190-TemanSawit/TemanSawit-ml-api.git
```
2. Install the required libraries from requirements.txt.
```bash
pip install -r requirements.txt
```
3. Navigate to the directory.
4. Run the following command in the directory terminal:
```bash
python .\server.py
```
or
```bash
python3 .\server.py
```
5. After the application startup complete, send a request to ```http://localhost:5000/recommend``` with a ```gender_product``` and ```city``` request, for example:
```JSON
{
"gender_product" : "Men",
"city" : "Jakarta"
}
```
7. The api will return some recommendations.
