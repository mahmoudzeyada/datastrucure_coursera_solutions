# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here

        if len(self.finish_time) == 0:
            finish_time_res = request.arrived_at+request.time_to_process
            if finish_time_res != 0:
                self.finish_time.append(finish_time_res)
            return Response(False, request.arrived_at)

        elif len(self.finish_time) > 0:
            last_response = self.finish_time[-1]
            if request.arrived_at >= last_response:
                respone = Response(False, request.arrived_at)
                self.finish_time = []
                finish_time_res = request.arrived_at+request.time_to_process
                self.finish_time.append(finish_time_res)
                return respone

            for finish_time in self.finish_time:
                if finish_time > request.arrived_at:
                    break
                self.finish_time.pop(0)

            if len(self.finish_time) < self.size:

                finish_time_res = request.time_to_process+last_response
                self.finish_time.append(finish_time_res)
                response = Response(False, last_response)
                return response

        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)
