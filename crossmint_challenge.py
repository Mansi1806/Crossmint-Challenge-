import requests
import json
import threading 
import time

def get_request(candidate_id):
    '''
    Returns the matrix of the goal map.

            Parameters:
                    candidate_id (str): A string

            Returns:
                    matrix (list): goal map conversted in the matrix with ceslestial objects in the order
    '''
    api_url = "https://challenge.crossmint.io/api/map/" + candidate_id +"/goal"
    response = requests.get(api_url)
    matrix = response.json()['goal']
    return matrix


def post_request_polyanets(candidate_id, row, col):
    '''
    No return as it is a post request to create a polynet at a paticular position.

            Parameters:
                    candidate_id (str): A string
                    row (int): An integer
                    col (int): An integer

    '''
    api_url = "https://challenge.crossmint.io/api/polyanets" 
    data = {"row": row, "column": col,"candidateId":candidate_id }
    headers =  {"Content-Type":"application/json"}
    requests.post(api_url, data=json.dumps(data), headers=headers)
   

def post_request_soloons(candidate_id, row, col, color):
    '''
    No return as it is a post request to create a soloon at a paticular position with a particular color.

            Parameters:
                    candidate_id (str): A string
                    row (int): An integer
                    col (int): An integer
                    color (str) : A string

    '''
    api_url = "https://challenge.crossmint.io/api/soloons" 
    data = {"row": row, "column": col,"color": color, "candidateId":candidate_id }
    headers =  {"Content-Type":"application/json"}
    requests.post(api_url, data=json.dumps(data), headers=headers)

def post_request_comeths(candidate_id , row, col, dir):
     '''
    No return as it is a post request to create a cometh at a paticular position and direction.

            Parameters:
                    candidate_id (str): A string
                    row (int): An integer
                    col (int): An integer
                    dir (str) : A string

    '''
    api_url = 'https://challenge.crossmint.io/api/comeths'
    data = {"row": row, "column": col,"direction": dir, "candidateId":candidate_id }
    headers =  {"Content-Type":"application/json"}
    requests.post(api_url, data=json.dumps(data), headers=headers)

  

def main():
    lock = threading.Lock()
    candidate_id = "14b77970-b23a-4b87-8a77-c060580eb68a"
    matrix = get_request(candidate_id)
    
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            lock.acquire() # To avoid race conditions
            if matrix[i][j] != "SPACE":

                string = matrix[i][j].lower()
                if string == "polyanet":
                    post_request_polyanets(candidate_id, i, j)

                string = string.split("_")
                param = k[0]
            
                obj = string[-1]
                if obj == "soloon":
                    post_request_soloons(candidate_id ,i, j, param)
                else:
                    post_request_comeths(candidate_id ,i, j ,param)
                time.sleep(3) # To avoid too many request at the same time
            lock.release()


if __name__ == "__main__":
    main()