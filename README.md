# Recout-ML-API

Description....

**Method:**
>POST

## **Recommendation Model**
```bash
POST {{Host}}/recommend
```
- **Body raw:**
```JSON
{
    "gender_product" : "Men",
    "city" : "Jakarta"
}
```
**Response:**
```JSON
[
    {
        "city": "Jakarta",
        "gender_product": "Men",
        "link": "http://assets.myntassets.com/v1/images/style/properties/01dbbbcddf07e76cb9eeb46db9f42606_images.jpg",
        "productDisplayName": "Classic Polo Men's Black With White Stripes T-shirt",
        "product_id": 4095,
        "temperature": "Hot",
        "usage": "Casual"
    },
]
```
**Note:** the block shown above shows 1 out of 5 recommendations.

## Steps
1. Clone the git repository.
```bash
git clone https://github.com/C241-PS139/Recout-ML-API.git
```
2. Install the required libraries from requirements.txt.
```bash
pip install -r requirements.txt
```
3. Navigate to the directory.
4. Run the following command in the directory terminal:
```bash
python server.py
```
5. After the application startup complete, send a request to ```http://localhost:5000/recommend``` as shown above.
6. The API will return some recommendations.
