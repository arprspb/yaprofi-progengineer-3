from fastapi import FastAPI
from user_filter import filter_users

from fastapi.responses import JSONResponse

app =FastAPI()

@app.get('/filter')
def get_filtered_users(input_string: str | None):
    return JSONResponse(content={"users": filter_users(input_string)}, status_code=200)

