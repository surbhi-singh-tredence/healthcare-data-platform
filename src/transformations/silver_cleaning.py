from pyspark.sql import DataFrame
from pyspark.sql.functions import trim, regexp_replace, lower
from utils.logger import get_logger


logger = get_logger("silver_cleaning")


def clean_data(df: DataFrame) -> DataFrame:
    """
    Perform data cleaning on healthcare QA dataset.

    Args:
        df: Raw Bronze DataFrame

    Returns:
        Cleaned DataFrame
    """

    try:

        logger.info("Starting data cleaning process")

        # Remove duplicate records
        df = df.dropDuplicates()

        logger.info("Duplicates removed")

        # Trim whitespace from status column
        df = df.withColumn("status", trim("status"))

        # Fix datatype issues in sample_number
        df = df.withColumn(
            "sample_number",
            regexp_replace("sample_number", "_err", "")
        )

        logger.info("Datatype issues fixed")

        # Standardize product column
        df = df.withColumn(
            "product",
            lower("product")
        )

        logger.info("Product column standardized")

        # Handle null values
        df = df.fillna({
            "status": "unknown",
            "product": "unknown"
        })

        logger.info("Null values handled")

        return df

    except Exception as e:

        logger.error(f"Error during Silver transformation: {str(e)}")
        raise


def write_silver_table(
    df: DataFrame,
    table_name: str
):
    """
    Write cleaned dataframe to Silver Delta table.
    """

    try:

        logger.info(f"Writing data to Silver table: {table_name}")

        (
            df.write
            .format("delta")
            .mode("overwrite")
            .saveAsTable(table_name)
        )

        logger.info("Silver table write successful")

    except Exception as e:

        logger.error(f"Failed writing Silver table: {str(e)}")
        raise