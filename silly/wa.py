from fastapi.responses import FileResponse

@app.get("/")
async def route():
  return FileResponse("index.html")

from fastapi.responses import FileResponse

@app.get("/awa")
async def route():
  return FileResponse("awa.html")
  
