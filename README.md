### Image Comparer
simple http service to compare images using opencv2


#### How to build
```bash
docker build -t ic .
```

#### How to run
##### local build
```bash
docker run -p 1234:80 ic 
```
##### docker hub
```bash
docker run -p 1234:80 ramimoshe/image-comparer
```

#### How to use
Method: POST <br />
Route: compare<br />
Body: 
```json
   {
   "method": "Correlation | Chi-Squared | Intersection | Hellinger",
   "imageUrl1": "link to image 1",
   "imageUrl2": "link to image 2"
   }
``` 

##### Example
```bash
curl -X POST \
  http://localhost:1234/compare \
  -H 'Content-Type: application/json' \
  -d '{
    "method": "Chi-Squared",
    "imageUrl1": "https://example.com/image1.png",
    "imageUrl2": "https://example.com/image2.png"
}'
```
