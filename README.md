# GPT-API-Fine-tuning   
## Store OPENAI_API_KEY     
```export OPENAI_API_KEY=your_api_key```
- Must run this to use OpenAI via CLI

## Fine-tuning Command   
```openai api fine_tunes.create -t ./dataset/gpt-4.jsonl -m davinci --suffix "GPT-4 v1"```
- Starts the fine-tuning Process
- Data must be a JSONL file, following the -t flag
- Base model can be one of [ada, babbage, curie, davinci]
- The model name can be set via suffix

## Resume Stream   
```openai api fine_tunes.follow -i <job_id>```
- Streams the process in the command line
- This information includes
    - job_id
    - cost
    - status (queued)
    - Fine-tune started
    - Completed Epochs
    - Succeeded

## List all created fine-tunes   
```openai api fine_tunes.list```

## Retreive state of fine-tune   
```openai api fine_tunes.get -i <job_id>```
- "fine_tuned_model" field is populated if the status is complete

## Prepare the dataset
```python3 prepare.py```

## Processing
- Removed redundant spaces
- Removed empty strings
- Removed strings with length less than 20