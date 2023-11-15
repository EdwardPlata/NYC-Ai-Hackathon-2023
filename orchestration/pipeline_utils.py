# Re-importing and setting up logging
import logging
logging.basicConfig(level=logging.INFO)

# Re-defining the classes and transformations

class Event:
    def __init__(self, data):
        self.data = data

class Node:
    def __init__(self, event=None):
        self.event = event
        self.next = None


class UnifiedPipelineManager:
    def __init__(self, transformations=[]):
        self.transformations = transformations
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue_event(self, event):
        new_node = Node(event)
        if self.rear is None:
            self.front = self.rear = new_node
            logging.info(f"Enqueued {event.data}. Queue is now initialized.")
            return
        self.rear.next = new_node
        self.rear = new_node
        logging.info(f"Enqueued {event.data}")

    def dequeue_event(self):
        if self.is_empty():
            logging.error("Attempted to dequeue from an empty queue.")
            raise Exception("Queue is empty.")
        removed_node = self.front
        self.front = removed_node.next
        if self.front is None:
            self.rear = None
        logging.info(f"Dequeued {removed_node.event.data}")
        return removed_node.event

    def validate_transformation(self, transform):
        if not callable(transform):
            logging.error(f"Invalid transformation: {transform}. It's not callable.")
            raise ValueError(f"Transformation {transform} is not a valid function.")
        
    def add_transformation(self, transform):
        self.validate_transformation(transform)
        self.transformations.append(transform)
        logging.info(f"Added transformation: {transform.__name__}")

    def apply_transformations(self, event):
        for transform in self.transformations:
            transform_name = transform.__name__
            try:
                new_data = transform(event.data)
                if hasattr(event, 'state') and transform_name in event.state and event.state[transform_name] != new_data:
                    logging.warning(f"Transformation {transform_name} resulted in a state change for {event.data}.")
                event.data = new_data
                if not hasattr(event, 'state'):
                    event.state = {}
                event.state[transform_name] = new_data
            except Exception as e:
                logging.error(f"Failed to apply transformation {transform_name} on {event.data}. Error: {e}")
        return event

    def process_pipeline(self, num_events):
        # Simulate ingestion of events
        for i in range(1, num_events + 1):
            event = Event(f"RawEvent-{i}")
            logging.info(f"Ingesting {event.data}")
            self.enqueue_event(event)

        # Process events
        while not self.is_empty():
            event = self.dequeue_event()
            event = self.apply_transformations(event)


