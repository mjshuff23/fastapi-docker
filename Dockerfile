# Pull base image
FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

EXPOSE 8000

# Install Next.js Dependencies
FROM node:lts as dependencies
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install

# Build Nextjs
FROM node:lts as builder
WORKDIR /frontend
COPY frontend ./
COPY --from=dependencies frontend/node_modules ./node_modules
RUN npm run build

# Configure ENV variables
FROM node:lts as runner
WORKDIR /frontend
ENV NODE_ENV production

COPY --from=builder /frontend/public ./public
COPY --from=builder /frontend/.next ./.next
COPY --from=builder /frontend/node_modules ./node_modules
COPY --from=builder /frontend/package.json ./package.json

EXPOSE 3000
