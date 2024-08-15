# LLM Inference Benchmark

This repository contains a Python script `llm_inference_benchmark.py` for benchmarking LLM inference servers.

## Prerequisites

- Python 3.6 or higher

## Configuration

Before running the script, you need to configure the following variables in the `llm_inference_benchmark.py` file:

- `KEY`: This is your API key. Replace `"APIKEY"` with your actual API key.

- `API_MODELS`: This is a dictionary where the keys are the API endpoints and the values are lists of models associated with each endpoint. For example:

    ```python
    API_MODELS = {
        "https://api.arliai.com/v1/chat/completions": ["Meta-Llama-3.1-8B-Instruct"]
    }
    ```

- `SESSION`: This is the session number. Set it to your desired session number.

## Running the Script

After configuring the variables, you can run the script with the following command:

```bash
python llm_inference_benchmark.py
```

## Example Output

Here is an example output from running the script:

```
===Testing prompt generation using 2 sessions and testing 1 prompts with 1 models.===

---[Thread 0, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1, 48 tokens long] Generation stats: time 22.194s, 1024 tokens, 46.1 tokens/s---
---[Thread 1, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1, 48 tokens long] Generation stats: time 22.194s, 1024 tokens, 46.1 tokens/s---

Generated 2048 tokens in 22.199 seconds.
Aggregate across all 2 sessions: 92.2 tokens/s
Individual sessions: Min: 46.1 tokens/s, Max: 46.1 tokens/s
Average completion time per thread: 22.194 seconds

===Testing prompt ingestion using 2 sessions and testing 1 prompts with 1 models.===

---[Thread 1, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1] Ingestion stats: time 2.659s, 4029 tokens, 1515.2 tokens/s---
---[Thread 0, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1] Ingestion stats: time 2.661s, 4029 tokens, 1514.1 tokens/s---

Ingested 8058 tokens in 2.664 seconds.
Aggregate across all 2 sessions: 3029.3 tokens/s
Individual sessions: Min: 1514.1 tokens/s, Max: 1515.2 tokens/s
Average ingestion time per session: 2.66 seconds

===Testing long context generation using 2 sessions and testing 1 prompts with 1 models.===

---[Thread 1, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1, 4029 tokens long] Generation stats: time 22.462s, 1024 tokens, 45.6 tokens/s---
---[Thread 0, API: https://api.arliai.com/v1/chat/completions, Model: Meta-Llama-3.1-8B-Instruct, Prompt 1, 4029 tokens long] Generation stats: time 22.462s, 1024 tokens, 45.6 tokens/s---

Generated 2048 tokens in 25.126 seconds.
Aggregate across all 2 sessions: 91.2 tokens/s
Individual sessions: Min: 45.6 tokens/s, Max: 45.6 tokens/s
Average generation time per session: 25.122 seconds
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
