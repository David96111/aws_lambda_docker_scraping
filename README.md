# Build and Run Image 
  `docker build -t app .`
  `docker run -p 9000:8080 app`

# Local Test
`curl --header "Content-Type: application/json" --request POST --data '{}' http://localhost:9000/2015-03-31/functions/function invocations`