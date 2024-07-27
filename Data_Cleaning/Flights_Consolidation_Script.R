library(tidyverse)
library(data.table)
airports <- c("ATL", "DFW", "DEN", "ORD", "LAX", "CLT", "MCO", "LAS", "PHX", "MIA")
airlines <- c("AA", "DL", "UA", "WN", "AS", "B6", "NK", "F9", "G4", "HA")

jan2023 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_01-2023.csv")
jan2023 <- jan2023 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

feb2023 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_02-2023.csv")
feb2023 <- feb2023 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

mar2023 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_02-2023.csv")
mar2023 <- mar2023 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

apr2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_04-2022.csv")
apr2022 <- apr2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

may2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_05-2022.csv")
may2022 <- may2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

jun2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_06-2022.csv")
jun2022 <- jun2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

jul2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_07-2022.csv")
jul2022 <- jul2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

aug2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_08-2022.csv")
aug2022 <- aug2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

sep2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_09-2022.csv")
sep2022 <- sep2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

oct2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_10-2022.csv")
oct2022 <- oct2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

nov2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_11-2022.csv")
nov2022 <- nov2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))

dec2022 <- read.csv("D:/Blue-04/Github/Data_Files/Months/Flight_data_12-2022.csv")
dec2022 <- dec2022 %>%  filter((Origin %in% airports) & (IATA_Code_Operating_Airline %in% airlines))


master_flights <- rbind(apr2022, may2022, jun2022, jul2022, aug2022, sep2022, oct2022, nov2022, dec2022, jan2023, feb2023, mar2023)

fwrite(master_flights, file="D:/Blue-04/Github/Data_Files/Flight_data_MASTER.csv")

