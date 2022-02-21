## Project Description
This python based module is used for getting the currency exchange rate between two currencies. Basically the module has class and methods which receives currency pair symbols and the amount.
This project uses modules such as requests, json, sys, os.



#### Some Explanation
There is a test python file written in the tests directory as follows:

```
fixer_api   = FixerAPI()
response    = fixer_api.get_result_amount("USD", "GBP", 100)
```

Here fixer_api is the object created and is responsible for calling the method dealing with API <br>

Then get_result_amount is called to get the amount of GBP that the user could buy with 100 USD


In `FixerAPI` class, the API call will execute continously as it uses Retry. Here as a test the number of times the request called will be 1000. It could be changed to any other required value. 

NB: Please note before running the test create an environment variable as below:

`export ACCESS_KEY=<YOUR_API_ACCESS_KEY>`

