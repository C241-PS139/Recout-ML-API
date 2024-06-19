# Recout-ML-API

Description....

**Method:**
>POST

- **Recommendation Model**
```bash
POST {{Host}}/recommend
```
**Response:**

```JSON
    {
    "classes": [
        "empty_bunch",
        "overripe",
        "ripe",
        "rotten",
        "underripe",
        "unripe"
    ],
    "prob": [
        6.216210022103041e-05,
        0.025118131190538406,
        0.6271576285362244,
        7.381191971944645e-05,
        0.3363390564918518,
        0.011249292641878128
    ],
    "top_2": {
        "ripe": 0.6271576285362244,
        "underripe": 0.3363390564918518
    }
  }
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
6. The API will return some recommendations.
