from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    data = {"Hello": "world"}
    return data

@app.get('/my_name')
async def my_name():
    data = "Thnnathat Chaiphutha"
    return data

@app.get("/input_name")
async def input_name(name):
    data = name
    return data

@app.get("/full_name")
async def full_name(fname, lname):
    data = "%s %s" %(fname, lname)
    return data

@app.get("/velocity_calculator")
async def velocity_calculator(s: float, t: float):
    velocity = "S : %.2f/T : %.2f  Valocity = %.2f"%(s,t,s/t)
    return velocity

@app.get("/s")
async def s(v,t):
    try:
        data = float(v)*float(t)
    except:
        data = {"error": True}
    return data

@app.get("/resistance")
async def resistance(r1: float, r2: float, r3: float):
    resistance_p = "r1 = %.2f ohm, r2 = %.2f ohm, r3 = %.2f ohm Resistance = %.2f ohm" %(r1,r2,r3,(1/r1+1/r2+1/r3)**-1)
    resistance_s = "r1 = %.2f ohm, r2 = %.2f ohm, r3 = %.2f ohm Resistance = %.2f ohm" %(r1,r2,r3,r1+r2+r3)
    return {"parallel": resistance_p, "series": resistance_s}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)