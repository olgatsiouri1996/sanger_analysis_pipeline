# Use Ubuntu as the base image
FROM ubuntu:latest
# Update and install dependencies
RUN apt-get update && \
    apt-get install -y r-base
# Install additional system dependencies
RUN apt-get install -y \
        libcurl4-openssl-dev \
        libssl-dev
# Install the latest version of pandoc
RUN apt-get install -y wget
RUN wget https://github.com/jgm/pandoc/releases/download/2.13/pandoc-2.13-1-amd64.deb && \
    dpkg -i pandoc-2.13-1-amd64.deb && \
    rm pandoc-2.13-1-amd64.deb
# Install BiocManager and sangeranalyseR packages
RUN R -e 'if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager"); BiocManager::install("sangeranalyseR")'
# Create directories for mounts
RUN mkdir /ab1 /report /fasta
# Copy your R script into the container
COPY sanger_analysis.R /sanger_analysis.R
# Run your R script when the container starts
CMD ["Rscript", "/sanger_analysis.R"]
