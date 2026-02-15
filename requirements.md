# Requirements Document: Nyaya-Dwarpal (Digital Scrutiny Officer)

## Introduction

Nyaya-Dwarpal is a Kiro-powered agentic middleware system designed to eliminate "Registry Limbo" in the Indian Judicial System. The system transforms the court registry from a passive filing portal into an active, real-time auditor by automating document scrutiny, ensuring integrity through cryptographic verification, and performing substantive audits of legal pleadings. Built on AWS infrastructure, it leverages AI services to validate procedural compliance, detect tampering, and flag factual contradictions to accelerate case processing.

## Glossary

- **System**: The Nyaya-Dwarpal middleware platform
- **Scrutiny_Agent**: The automated document validation component
- **Integrity_Watchdog**: The chain-of-custody and tampering detection component
- **Audit_Agent**: The substantive fact-checking and case law verification component
- **E_Filing_Portal**: The external court e-filing system that uploads documents
- **CIS**: Case Information System containing FIRs and depositions
- **Remediation_Guide**: A document explaining defects and correction steps
- **Document_Hash**: SHA-256 cryptographic hash of a filed document
- **Immutable_Ledger**: AWS-backed or blockchain storage for document hashes
- **Hearing_Ready_Brief**: A prioritized case summary for judicial review
- **Textract**: AWS service for document text extraction
- **Bedrock**: AWS AI service for document analysis
- **Bhashini**: Indian government translation service for regional languages

## Requirements

### Requirement 1: Document Upload and Ingestion

**User Story:** As a court registry system, I want to receive and process uploaded legal documents, so that they can be validated and stored for judicial proceedings.

#### Acceptance Criteria

1. WHEN a document is uploaded via the E_Filing_Portal, THE System SHALL accept PDF and image formats (JPEG, PNG, TIFF)
2. WHEN a document is received, THE System SHALL extract metadata including case number, filing date, document type, and filer information
3. WHEN document extraction fails, THE System SHALL log the error and notify the E_Filing_Portal with a descriptive error message
4. WHEN a document is successfully ingested, THE System SHALL trigger the Scrutiny_Agent for validation

### Requirement 2: Automated Procedural Validation

**User Story:** As a court registry officer, I want documents to be automatically validated for procedural compliance, so that defective filings are identified immediately without manual review.

#### Acceptance Criteria

1. WHEN the Scrutiny_Agent receives a document, THE System SHALL use Textract to extract text and structural elements from the document
2. WHEN text extraction is complete, THE System SHALL use Bedrock to validate the presence of required signatures
3. WHEN text extraction is complete, THE System SHALL use Bedrock to validate court fee payment evidence
4. WHEN text extraction is complete, THE System SHALL use Bedrock to validate jurisdictional compliance
5. WHEN text extraction is complete, THE System SHALL use Bedrock to validate the presence of mandatory annexures
6. WHEN all validation checks pass, THE System SHALL mark the document as procedurally compliant
7. WHEN any validation check fails, THE System SHALL mark the document as defective and identify specific defects

### Requirement 3: Multilingual Remediation Guidance

**User Story:** As a document filer, I want to receive clear guidance in my regional language when my filing is defective, so that I can correct errors and refile quickly.

#### Acceptance Criteria

1. WHEN a document is marked as defective, THE System SHALL generate a Remediation_Guide listing all identified defects
2. WHEN generating a Remediation_Guide, THE System SHALL include specific instructions for correcting each defect
3. WHEN a Remediation_Guide is generated, THE System SHALL use Bhashini to translate the guide into the filer's preferred regional language
4. WHEN translation is complete, THE System SHALL deliver the Remediation_Guide to the E_Filing_Portal for filer notification
5. IF Bhashini translation fails, THEN THE System SHALL deliver the Remediation_Guide in English as a fallback

### Requirement 4: Cryptographic Hash Generation

**User Story:** As a judicial administrator, I want every validated document to have a cryptographic fingerprint, so that any tampering or modification can be detected.

#### Acceptance Criteria

1. WHEN a document passes procedural validation, THE System SHALL compute a SHA-256 Document_Hash of the complete document content
2. WHEN computing the hash, THE System SHALL include document metadata in the hash calculation
3. WHEN the Document_Hash is generated, THE System SHALL associate it with the case number and filing timestamp
4. WHEN hash generation fails, THE System SHALL log the error and retry up to three times before marking the document as unprocessable

### Requirement 5: Immutable Ledger Storage

**User Story:** As a judicial administrator, I want document hashes stored in an immutable ledger, so that the chain of custody is verifiable and tamper-proof.

#### Acceptance Criteria

1. WHEN a Document_Hash is generated, THE Integrity_Watchdog SHALL store the hash in the Immutable_Ledger
2. WHEN storing a hash, THE System SHALL record the case number, document type, filing timestamp, and filer information
3. WHEN a hash is successfully stored, THE System SHALL return a ledger transaction ID as proof of storage
4. WHEN ledger storage fails, THE System SHALL retry up to three times before alerting system administrators
5. THE System SHALL prevent modification or deletion of any entry in the Immutable_Ledger

### Requirement 6: Document Tampering Detection

**User Story:** As a judicial administrator, I want to be alerted if any filed document is modified after submission, so that evidence integrity is maintained.

#### Acceptance Criteria

1. WHEN a document's content or metadata is accessed for modification, THE Integrity_Watchdog SHALL recompute the SHA-256 hash
2. WHEN the recomputed hash differs from the stored Document_Hash, THE System SHALL flag the document as potentially tampered
3. WHEN tampering is detected, THE System SHALL generate a real-time alert to judicial administrators
4. WHEN tampering is detected, THE System SHALL log the detection event with timestamp, user identity, and hash mismatch details
5. WHEN a document is flagged as tampered, THE System SHALL prevent its use in judicial proceedings until reviewed

### Requirement 7: Substantive Pleading Analysis

**User Story:** As a judge, I want incoming pleadings analyzed against existing case records, so that factual contradictions are identified before the hearing.

#### Acceptance Criteria

1. WHEN a document passes procedural validation, THE Audit_Agent SHALL retrieve related FIRs and depositions from the CIS
2. WHEN case records are retrieved, THE System SHALL use Bedrock to compare factual claims in the pleading against existing records
3. WHEN factual contradictions are detected, THE System SHALL flag specific contradictory statements with references to source documents
4. WHEN no contradictions are found, THE System SHALL mark the pleading as factually consistent
5. IF CIS retrieval fails, THEN THE System SHALL log the error and proceed without substantive analysis

### Requirement 8: Case Law Verification

**User Story:** As a judge, I want cited case laws in pleadings verified against legal databases, so that I can trust the legal precedents referenced.

#### Acceptance Criteria

1. WHEN the Audit_Agent analyzes a pleading, THE System SHALL extract all cited case law references
2. WHEN case law references are extracted, THE System SHALL query legal databases to verify each citation exists
3. WHEN a citation cannot be verified, THE System SHALL flag it as potentially incorrect or hallucinated
4. WHEN a citation is verified, THE System SHALL confirm the citation's relevance to the legal point being argued
5. WHEN all citations are processed, THE System SHALL include verification results in the Hearing_Ready_Brief

### Requirement 9: Hearing-Ready Brief Generation

**User Story:** As a judge, I want a prioritized case summary with procedural and substantive analysis, so that I can efficiently prepare for hearings.

#### Acceptance Criteria

1. WHEN substantive analysis is complete, THE Audit_Agent SHALL generate a Hearing_Ready_Brief
2. WHEN generating the brief, THE System SHALL include procedural validation status
3. WHEN generating the brief, THE System SHALL include flagged factual contradictions with source references
4. WHEN generating the brief, THE System SHALL include case law verification results
5. WHEN generating the brief, THE System SHALL assign a trial readiness score based on procedural cleanliness and factual consistency
6. WHEN the brief is complete, THE System SHALL deliver it to the judicial case management system

### Requirement 10: Case Prioritization

**User Story:** As a court administrator, I want cases prioritized based on procedural and substantive readiness, so that hearing-ready cases are scheduled efficiently.

#### Acceptance Criteria

1. WHEN multiple cases are processed, THE System SHALL rank cases by trial readiness score
2. WHEN ranking cases, THE System SHALL prioritize cases with no procedural defects
3. WHEN ranking cases, THE System SHALL prioritize cases with no factual contradictions
4. WHEN ranking cases, THE System SHALL prioritize cases with verified case law citations
5. WHEN prioritization is complete, THE System SHALL provide a ranked case list to the court scheduling system

### Requirement 11: Error Handling and Logging

**User Story:** As a system administrator, I want comprehensive error logging and graceful failure handling, so that system issues can be diagnosed and resolved quickly.

#### Acceptance Criteria

1. WHEN any component encounters an error, THE System SHALL log the error with timestamp, component name, and error details
2. WHEN a critical error occurs, THE System SHALL send alerts to system administrators
3. WHEN an external service (Textract, Bedrock, Bhashini, CIS) is unavailable, THE System SHALL retry the operation with exponential backoff
4. WHEN retries are exhausted, THE System SHALL mark the document for manual review and notify administrators
5. THE System SHALL maintain error logs for a minimum of 90 days for audit purposes

### Requirement 12: Performance and Scalability

**User Story:** As a court administrator, I want the system to handle high document volumes during peak filing periods, so that processing delays are minimized.

#### Acceptance Criteria

1. WHEN document volume exceeds normal capacity, THE System SHALL scale processing resources automatically
2. WHEN a document is submitted, THE System SHALL complete procedural validation within 5 minutes
3. WHEN a document is submitted, THE System SHALL complete substantive analysis within 15 minutes
4. THE System SHALL support concurrent processing of at least 100 documents
5. WHEN system load is high, THE System SHALL queue documents and process them in submission order

### Requirement 13: Security and Access Control

**User Story:** As a security administrator, I want strict access controls and audit trails, so that sensitive judicial documents are protected from unauthorized access.

#### Acceptance Criteria

1. THE System SHALL authenticate all users and services using AWS IAM credentials
2. THE System SHALL enforce role-based access control for document access
3. WHEN a user accesses a document, THE System SHALL log the access event with user identity, timestamp, and document identifier
4. THE System SHALL encrypt all documents at rest using AES-256 encryption
5. THE System SHALL encrypt all data in transit using TLS 1.3 or higher
6. THE System SHALL maintain access logs for a minimum of 180 days for compliance auditing
