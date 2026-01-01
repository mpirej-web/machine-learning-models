package helpers

import (
	"fmt"
	"log"
	"os"
)

func PrintErrorAndExit(err error) {
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		log.Fatal(err)
	}
}

func GetEnvOrDefault(key, defaultVal string) string {
	val := os.Getenv(key)
	if val == "" {
		return defaultVal
	}
	return val
}