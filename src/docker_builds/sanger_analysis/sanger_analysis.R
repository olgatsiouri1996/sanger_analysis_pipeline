# insert library
library("sangeranalyseR")
# import input directory
setwd("/ab1")
# import the parameters file
parameters <- read.delim(file = "parameters.txt",header = F,sep = "\t",quote = "")
# Creating the Sanger Alignment object with the parameters
contigs <- SangerAlignment(
  printLevel = parameters[1,2],
  inputSource = parameters[2,2],
  processMethod = parameters[3,2],
  ABIF_Directory = parameters[4,2],
  FASTA_File = ifelse(parameters[5,2] == "NULL", NULL, parameters[5,2]),
  REGEX_SuffixForward = parameters[6,2],
  REGEX_SuffixReverse = parameters[7,2],
  CSV_NamesConversion = ifelse(parameters[8,2] == "NULL", NULL, parameters[8,2]),
  geneticCode = GENETIC_CODE,
  TrimmingMethod = parameters[10,2],
  M1TrimmingCutoff = ifelse(parameters[11,2] == "NULL", NULL, as.numeric(parameters[11,2])),
  M2CutoffQualityScore = ifelse(parameters[12,2] == "NULL", NULL, as.numeric(parameters[12,2])),
  M2SlidingWindowSize = ifelse(parameters[13,2] == "NULL", NULL, as.numeric(parameters[13,2])),
  baseNumPerRow = as.numeric(parameters[14,2]),
  heightPerRow = as.numeric(parameters[15,2]),
  signalRatioCutoff = as.numeric(parameters[16,2]),
  showTrimmed = as.logical(parameters[17,2]),
  refAminoAcidSeq = ifelse(parameters[18,2] == "NULL", "", parameters[18,2]),
  minReadsNum = as.numeric(parameters[19,2]),
  minReadLength = as.numeric(parameters[20,2]),
  minFractionCall = as.numeric(parameters[21,2]),
  maxFractionLost = as.numeric(parameters[22,2]),
  acceptStopCodons = as.logical(parameters[23,2]),
  readingFrame = as.numeric(parameters[24,2]),
  processorsNum = as.numeric(parameters[25,2])
)
# generate report
generateReport(contigs,outputDir = "/report")
# export to fasta
writeFasta(contigs,outputDir = "/fasta")