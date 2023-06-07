# -*- coding:utf-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder

class Memo(BaseModel):
  id:str
  content:str

memos = []
app = FastAPI()

@app.get("/memos")
def read_memo():
  return memos

@app.post("/memos")
def create_memo(memo: Memo):
  memos.append(memo)
  return 'Success'

@app.put("/memos/{memo_id}")
def put_memo(req_memo: Memo):
  for memo in memos:
    if memo.id == req_memo.id:
      memo.content=req_memo.content
      return "성공했습니다."
  return "해당되는 Id를 갖는 메모는 없습니다."

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
  for index, memo in enumerate(memos):
    if memo.id == memo_id:
      memos.pop(index)
      return "성공했습니다."
  return "해당되는 Id를 갖는 메모는 없습니다."

app.mount("/", StaticFiles(directory="static", html=True), name="static")
print("한글")
print(memos)

