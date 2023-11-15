# UnifiedPipelineManager Documentation

## Introduction:
The `UnifiedPipelineManager` class allows for the creation and management of a pipeline to process events. Events can be ingested, transformed using a series of transformations, and then processed. The pipeline utilizes a queue to manage the flow of events, ensuring a first-in-first-out (FIFO) processing paradigm.

## Classes:

### Event
- **Purpose**: Represents the data that will undergo processing.
- **Properties**:
    - `data`: The content of the event.

### Node
- **Purpose**: Represents an element in the queue, facilitating the FIFO approach.
- **Properties**:
    - `event`: The `Event` object that this node holds.
    - `next`: Reference to the subsequent `Node` in the queue.

### UnifiedPipelineManager
- **Purpose**: Orchestrates the entire pipeline process from ingestion to processing.

## Methods:

### 1. `is_empty(self)`
- **Description**: Determines if the queue is currently empty.
- **Returns**: `True` if the queue is empty, `False` otherwise.

### 2. `enqueue_event(self, event)`
- **Description**: Inserts an event into the end of the queue.
- **Parameters**:
    - `event`: The `Event` object to be enqueued.

### 3. `dequeue_event(self)`
- **Description**: Retrieves and removes the front event from the queue.
- **Returns**: The dequeued `Event` object.

### 4. `validate_transformation(self, transform)`
- **Description**: Validates whether a given transformation function is callable.
- **Parameters**:
    - `transform`: The transformation function to validate.

### 5. `add_transformation(self, transform)`
- **Description**: Appends a transformation function to the internal list of transformations.
- **Parameters**:
    - `transform`: The transformation function to be added.

### 6. `apply_transformations(self, event)`
- **Description**: Sequentially applies all transformations to a provided event.
- **Parameters**:
    - `event`: The `Event` object to which transformations will be applied.

### 7. `process_pipeline(self, num_events)`
- **Description**: Simulates the ingestion of a certain number of events and processes them sequentially through the pipeline.
- **Parameters**:
    - `num_events`: The quantity of events to be ingested and processed.

## Usage:

1. **Initialization**:
   ```python
   # Instantiate the pipeline manager
   pipeline = UnifiedPipelineManager()
   # Example transformations
   def transform_to_upper(data):
       return data.upper()
    
   def add_prefix(data):
       return f"Transformed-{data}"
    
   # Register transformations to the pipeline
pipeline.add_transformation(transform_to_upper)
pipeline.add_transformation(add_prefix)
    ```

## Simulate ingestion and processing of 5 events
```python
pipeline.process_pipeline(5)
```