# Mixtral installation

Original [README](./README.orig.md)

## Repo

https://github.com/ggerganov/llama.cpp

### Models Mixtral

https://huggingface.co/TheBloke/openbuddy-mixtral-7bx8-v16.3-32k-GGUF

## Requirements

```bash
brew install open-mpi
brew install wget
brew install git
```

## Installation

```bash
git clone --depth 1 git@github.com:ggerganov/llama.cpp.git -b mixtral
cd llama.cpp
make
# 7GB size 508 token prompt
wget https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/resolve/main/mixtral-8x7b-instruct-v0.1.Q2_K.gguf
make -j && ./main -m models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf -p "Building a website can be done in 10 simple steps:\nStep 1:" -e --ctx-size 0
make -j && ./main -m models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf -p "What's a 'number of tokens to predict' in LLAMA.ccp" -e --ctx-size 0


# or openbuddy-mixtral-7bx8-v16.3-32k.Q8_0.gguf exhaust Mac M3 max memory - 32Go
wget https://huggingface.co/TheBloke/openbuddy-mixtral-7bx8-v16.3-32k-GGUF/resolve/main/openbuddy-mixtral-7bx8-v16.3-32k.Q5_K_M.gguf
# or openbuddy-mixtral-7bx8-v16.3-32k.Q8_0.gguf exhaust Mac M3 max memory - 32Go
wget https://huggingface.co/TheBloke/openbuddy-mixtral-7bx8-v16.3-32k-GGUF/resolve/main/openbuddy-mixtral-7bx8-v16.3-32k.Q8_0.gguf
# or openbuddy-mixtral-7bx8-v16.3-32k.Q8_0.gguf exhaust Mac M3 max memory - 32Go
wget https://huggingface.co/TheBloke/openbuddy-mixtral-7bx8-v16.3-32k-GGUF/resolve/main/openbuddy-mixtral-7bx8-v16.3-32k.Q4_K_M.gguf
```

## Properties

```
  -c N, --ctx-size N    size of the prompt context (default: 512, 0 = loaded from model)
  -n N, --n-predict N   number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled) Number of token in the output
  -e, --escape          process prompt escapes sequences (\n, \r, \t, \', \", \\)
  -b N, --batch-size N  batch size for prompt processing (default: 512)
```

## Other features that might be use full

https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#constrained-output-with-grammars
llama.cpp supports grammars to constrain model output. For example, you can force the model to output JSON only:

```bash
./main -m ./models/13B/ggml-model-q4_0.gguf -n 256 --grammar-file grammars/json.gbnf -p 'Request: schedule a call at 8pm; Command:'
```

## Tries

```bash
# exhaust Mac M3 max memory - 32Go
make -j && ./main -m models/openbuddy-mixtral-7bx8-v16.3-32k.Q8_0.gguf -p "CONTENT HERE" -e --ctx-size 0

# exhaust Mac M3 max memory - 32Go
make -j && ./main -m models/openbuddy-mixtral-7bx8-v16.3-32k.Q5_K_M.gguf -p "CONTENT HERE" -e --ctx-size 0

# exhaust Mac M3 max memory - 32Go
make -j && ./main -m models/openbuddy-mixtral-7bx8-v16.3-32k.Q4_K_M.gguf -p "CONTENT HERE" -e --ctx-size 0

```
