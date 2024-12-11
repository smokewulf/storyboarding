from fastapi import FastAPI

app = FastAPI()                                                                                                                        
                                                                                                                                          
@app.get('/teamspace/studios/this_studio/storyboarding')                                                                               
async def storyboarding():                                                                                                             
    return {'message': 'Welcome to the Storyboarding Studio!'}                                                                         
                                                                                                                                          
if __name__ == '__main__':                                                                                                             
       import uvicorn
       uvicorn.run(app, host='127.0.0.1', port=8000)