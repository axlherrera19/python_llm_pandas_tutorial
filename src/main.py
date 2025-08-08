
import io
import os
import uvicorn
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# print("Manually injecting GEMINI API KEY " + os.getenv("GEMINI_API_KEY")) # type: ignore
print("Path " + os.getenv("PATH")) # type: ignore



from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()



@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}


@app.post("/calculate-statistics")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        return {"error": "El archivo debe ser un CSV"}
    
    # Leer el contenido del archivo CSV
    contents = await file.read()
    results = {}
    # Convertir el contenido a un DataFrame de pandas
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    for col in df.columns:
        stats = get_dataframe_stats(df, col)
        results.setdefault(col,stats)
    return {
        "filename": file.filename,
        "columns": df.columns.tolist(),
        "rows": len(df),
        "stats": results
    }


def get_dataframe_stats(dataframe, field):
    print("*************Stats*************")
    print(f"Stats for {field}")
    stats = {
        "mean": float(dataframe[field].mean()),
        "median": float(dataframe[field].median()),
        "max": float(dataframe[field].max()),
        "min": float(dataframe[field].min()),
        "mode": float(dataframe[field].mode())
    }
    # stats_dataframe = pd.DataFrame(stats)
    # print(stats_dataframe)
    print("*************END: Stats*************")
    return stats


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)