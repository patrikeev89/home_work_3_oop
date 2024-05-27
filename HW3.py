class StudyGroup:
    
    pass

class Stream:
    def __init__(self, study_groups):
        self.study_groups = study_groups

    def __iter__(self):
        return iter(self.study_groups)

    def get_study_groups(self):
        return self.study_groups



class StreamComparator:
    @staticmethod
    def compare(stream1, stream2):
        return len(stream1.get_study_groups()) - len(stream2.get_study_groups())



class StreamService:
    def sort_streams(self, streams):
        streams.sort(key=lambda stream: len(stream.get_study_groups()))



class Controller:
    def __init__(self, stream_service):
        self.stream_service = stream_service

    def sort_streams(self, streams):
        self.stream_service.sort_streams(streams)

# Пример использования
if __name__ == "__main__":
    group1 = StudyGroup()
    group2 = StudyGroup()
    group3 = StudyGroup()

    stream1 = Stream([group1, group2])
    stream2 = Stream([group1])
    stream3 = Stream([group1, group2, group3])

    streams = [stream1, stream2, stream3]

    stream_service = StreamService()
    controller = Controller(stream_service)

    print("До сортировки:")
    for stream in streams:
        print(len(stream.get_study_groups()))

    controller.sort_streams(streams)

    print("После сортировки:")
    for stream in streams:
        print(len(stream.get_study_groups()))
