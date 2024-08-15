
FROM python:3.9-slim-bullseye AS build-stage


WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
    numpy==1.22.1 \
    onnxruntime \
    flask==3.0.3 \
    pillow==10.4.0 \
    torch==1.12.1+cpu \
    torchvision==0.13.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html


COPY . .


RUN apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && find /usr/local -depth -name '*.pyc' -delete


FROM python:3.9-slim-bullseye AS final-stage


WORKDIR /app

COPY --from=build-stage /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin
COPY --from=build-stage /app /app


EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
