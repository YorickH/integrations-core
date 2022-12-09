# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence, Union

from pydantic import BaseModel, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class Aws(BaseModel):
    class Config:
        allow_mutation = False

    instance_endpoint: Optional[str]


class Azure(BaseModel):
    class Config:
        allow_mutation = False

    deployment_type: Optional[str]
    name: Optional[str]


class Gcp(BaseModel):
    class Config:
        allow_mutation = False

    instance_id: Optional[str]
    project_id: Optional[str]


class MetricPatterns(BaseModel):
    class Config:
        allow_mutation = False

    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]


class ObfuscatorOptions(BaseModel):
    class Config:
        allow_mutation = False

    collect_commands: Optional[bool]
    collect_comments: Optional[bool]
    collect_metadata: Optional[bool]
    collect_tables: Optional[bool]
    keep_dollar_quoted_func: Optional[bool]
    keep_sql_alias: Optional[bool]
    replace_digits: Optional[bool]


class QueryActivity(BaseModel):
    class Config:
        allow_mutation = False

    collection_interval: Optional[float]
    enabled: Optional[bool]
    payload_row_limit: Optional[float]


class QueryMetrics(BaseModel):
    class Config:
        allow_mutation = False

    collection_interval: Optional[float]
    enabled: Optional[bool]
    pg_stat_statements_max_warning_threshold: Optional[float]


class QuerySamples(BaseModel):
    class Config:
        allow_mutation = False

    collection_interval: Optional[float]
    enabled: Optional[bool]
    explain_function: Optional[str]
    explain_parameterized_queries: Optional[bool]
    explained_queries_cache_maxsize: Optional[int]
    explained_queries_per_hour_per_query: Optional[int]
    samples_per_hour_per_query: Optional[int]
    seen_samples_cache_maxsize: Optional[int]


class Relation(BaseModel):
    class Config:
        allow_mutation = False

    relation_name: Optional[str]
    relation_regex: Optional[str]
    relation_schema: Optional[str]
    relkind: Optional[Sequence[str]]
    schemas: Optional[Sequence[str]]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    application_name: Optional[str]
    aws: Optional[Aws]
    azure: Optional[Azure]
    collect_activity_metrics: Optional[bool]
    collect_bloat_metrics: Optional[bool]
    collect_count_metrics: Optional[bool]
    collect_database_size_metrics: Optional[bool]
    collect_default_database: Optional[bool]
    collect_function_metrics: Optional[bool]
    collect_wal_metrics: Optional[bool]
    custom_queries: Optional[Sequence[Mapping[str, Any]]]
    data_directory: Optional[str]
    dbm: Optional[bool]
    dbname: Optional[str]
    dbstrict: Optional[bool]
    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    gcp: Optional[Gcp]
    host: str
    ignore_databases: Optional[Sequence[str]]
    log_unobfuscated_plans: Optional[bool]
    log_unobfuscated_queries: Optional[bool]
    max_relations: Optional[int]
    metric_patterns: Optional[MetricPatterns]
    min_collection_interval: Optional[float]
    obfuscator_options: Optional[ObfuscatorOptions]
    password: Optional[str]
    pg_stat_statements_view: Optional[str]
    port: Optional[int]
    query_activity: Optional[QueryActivity]
    query_metrics: Optional[QueryMetrics]
    query_samples: Optional[QuerySamples]
    query_timeout: Optional[int]
    relations: Optional[Sequence[Union[str, Relation]]]
    reported_hostname: Optional[str]
    service: Optional[str]
    ssl: Optional[str]
    ssl_cert: Optional[str]
    ssl_key: Optional[str]
    ssl_password: Optional[str]
    ssl_root_cert: Optional[str]
    table_count_limit: Optional[int]
    tag_replication_role: Optional[bool]
    tags: Optional[Sequence[str]]
    username: str

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
